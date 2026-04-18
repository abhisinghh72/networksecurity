from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException 
from networksecurity.logging.logger import logging 
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH

from scipy.stats import ks_2samp
import pandas as pd
import os, sys

from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file


class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def validate_number_of_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            expected_columns = list(self._schema_config["columns"].keys())
            actual_columns = list(dataframe.columns)

            logging.info(f"Expected columns: {expected_columns}")
            logging.info(f"Actual columns: {actual_columns}")

            # Count check
            if len(actual_columns) != len(expected_columns):
                logging.info("Column count mismatch")
                return False

            # Missing / Extra check
            missing_cols = set(expected_columns) - set(actual_columns)
            extra_cols = set(actual_columns) - set(expected_columns)

            if missing_cols:
                logging.info(f"Missing columns: {missing_cols}")
                return False

            if extra_cols:
                logging.info(f"Unexpected columns: {extra_cols}")
                return False

            return True

        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def detect_dataset_drift(self, base_df, current_df, threshold=0.05) -> bool:
        try:
            status = True
            report = {}

            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]

                test = ks_2samp(d1, d2)

                if test.pvalue < threshold:
                    drift_found = True
                    status = False
                else:
                    drift_found = False

                report[column] = {
                    "p_value": float(test.pvalue),
                    "drift_status": drift_found
                }

            drift_report_file_path = self.data_validation_config.drift_report_file_path

            os.makedirs(os.path.dirname(drift_report_file_path), exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path, content=report)

            return status

        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            train_dataframe = self.read_data(train_file_path)
            test_dataframe = self.read_data(test_file_path)

            validation_status = True

            # Column Validation
            if not self.validate_number_of_columns(train_dataframe):
                logging.info("Train column validation FAILED")
                validation_status = False
            else:
                logging.info("Train column validation PASSED")

            if not self.validate_number_of_columns(test_dataframe):
                logging.info("Test column validation FAILED")
                validation_status = False
            else:
                logging.info("Test column validation PASSED")

            # Drift Check (Monitoring Only) 
            drift_status = self.detect_dataset_drift(
                base_df=train_dataframe,
                current_df=test_dataframe
            )

            if not drift_status:
                logging.info("Data drift detected (monitoring only)")
            else:
                logging.info("No data drift detected")

            # Save only if valid
            if validation_status:
                os.makedirs(
                    os.path.dirname(self.data_validation_config.valid_train_file_path),
                    exist_ok=True
                )

                train_dataframe.to_csv(
                    self.data_validation_config.valid_train_file_path,
                    index=False,
                    header=True
                )

                test_dataframe.to_csv(
                    self.data_validation_config.valid_test_file_path,
                    index=False,
                    header=True
                )

                valid_train_path = self.data_validation_config.valid_train_file_path
                valid_test_path = self.data_validation_config.valid_test_file_path
            else:
                logging.info("Validation failed. Skipping saving valid files.")
                valid_train_path = None
                valid_test_path = None

            #Artifact
            data_validation_artifact = DataValidationArtifact(
                validation_status=validation_status,
                valid_train_file_path=valid_train_path,
                valid_test_file_path=valid_test_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
            )

            return data_validation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)