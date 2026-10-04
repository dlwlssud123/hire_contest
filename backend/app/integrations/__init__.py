from app.integrations.employment24 import (
    employment24_recruit_client,
    employment24_job_info_client,
    employment24_psych_test_client,
    employment24_training_client,
)
from app.integrations.qnet import qnet_cert_client
from app.integrations.corporate import corporate_data_client

__all__ = [
    "employment24_recruit_client",
    "employment24_job_info_client",
    "employment24_psych_test_client",
    "employment24_training_client",
    "qnet_cert_client",
    "corporate_data_client",
]
