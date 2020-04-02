import urllib3

import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from settings import Settings


class Isilon:
    def __init__(self, api_class=""):
        config = Settings()
        urllib3.disable_warnings()

        # Configuration Settings
        url = f"https://{config.hostname}:{config.port}"
        configuration = isi_sdk_8_2_1.Configuration()
        configuration.host = url
        configuration.username = config.username
        configuration.password = config.password
        configuration.verify_ssl = config.verify_ssl

        # Create an instance of the API class
        api_client = isi_sdk_8_2_1.ApiClient(configuration)

        if api_class == "AntivirusApi":
            raise ApiException("Not implemented in this class")

        elif api_class == "AuditApi":
            raise Exception("Not implemented in this class")

        elif api_class == "AuthApi":
            raise Exception("Not implemented in this class")

        elif api_class == "AuthGroupsApi":
            raise Exception("Not implemented in this class")

        elif api_class == "AuthRolesApi":
            raise Exception("Not implemented in this class")

        elif api_class == "AuthUsersApi":
            raise Exception("Not implemented in this class")

        elif api_class == "CertificateApi":
            raise Exception("Not implemented in this class")

        elif api_class == "CloudApi":
            raise Exception("Not implemented in this class")

        elif api_class == "ClusterApi":
            raise Exception("Not implemented in this class")

        elif api_class == "ClusterNodesApi":
            raise Exception("Not implemented in this class")

        elif api_class == "DebugApi":
            raise Exception("Not implemented in this class")

        elif api_class == "DedupeApi":
            raise Exception("Not implemented in this class")

        elif api_class == "EventApi":
            raise Exception("Not implemented in this class")

        elif api_class == "FileFilterApi":
            raise Exception("Not implemented in this class")

        elif api_class == "FilepoolApi":
            raise Exception("Not implemented in this class")

        elif api_class == "FilesystemApi":
            raise Exception("Not implemented in this class")

        elif api_class == "FsaApi":
            raise Exception("Not implemented in this class")

        elif api_class == "FsaIndexApi":
            raise Exception("Not implemented in this class")

        elif api_class == "FsaResultsApi":
            raise Exception("Not implemented in this class")

        elif api_class == "GroupnetsSummaryApi":
            raise Exception("Not implemented in this class")

        elif api_class == "HardeningApi":
            raise Exception("Not implemented in this class")

        elif api_class == "HardwareApi":
            raise Exception("Not implemented in this class")

        elif api_class == "HealthcheckApi":
            raise Exception("Not implemented in this class")

        elif api_class == "IdResolutionApi":
            raise Exception("Not implemented in this class")

        elif api_class == "IdResolutionZonesApi":
            raise Exception("Not implemented in this class")

        elif api_class == "JobApi":
            raise Exception("Not implemented in this class")

        elif api_class == "LicenseApi":
            raise Exception("Not implemented in this class")

        elif api_class == "LocalApi":
            raise Exception("Not implemented in this class")

        elif api_class == "LocalClusterApi":
            raise Exception("Not implemented in this class")

        elif api_class == "NamespaceApi":
            raise Exception("Not implemented in this class")

        elif api_class == "NetworkApi":
            raise Exception("Not implemented in this class")

        elif api_class == "NetworkGroupnetsApi":
            raise Exception("Not implemented in this class")

        elif api_class == "NetworkGroupnetsSubnetsApi":
            raise Exception("Not implemented in this class")

        elif api_class == "PerformanceApi":
            raise Exception("Not implemented in this class")

        elif api_class == "PerformanceDatasetsApi":
            raise Exception("Not implemented in this class")

        elif api_class == "ProtocolsApi":
            raise Exception("Not implemented in this class")

        elif api_class == "ProtocolsHdfsApi":
            raise Exception("Not implemented in this class")

        elif api_class == "QuotaApi":
            raise Exception("Not implemented in this class")

        elif api_class == "QuotaQuotasApi":
            raise Exception("Not implemented in this class")

        elif api_class == "QuotaReportsApi":
            raise Exception("Not implemented in this class")

        elif api_class == "RemotesupportApi":
            raise Exception("Not implemented in this class")

        elif api_class == "SnapshotApi":
            raise Exception("Not implemented in this class")

        elif api_class == "SnapshotChangelistsApi":
            raise Exception("Not implemented in this class")

        elif api_class == "StatisticsApi":
            self.api_client = isi_sdk_8_2_1.StatisticsApi(api_client)

        elif api_class == "StoragepoolApi":
            raise Exception("Not implemented in this class")

        elif api_class == "SyncApi":
            raise Exception("Not implemented in this class")

        elif api_class == "SyncPoliciesApi":
            raise Exception("Not implemented in this class")

        elif api_class == "SyncReportsApi":
            raise Exception("Not implemented in this class")

        elif api_class == "SyncServiceTargetApi":
            raise Exception("Not implemented in this class")

        elif api_class == "SyncTargetApi":
            raise Exception("Not implemented in this class")

        elif api_class == "UpgradeApi":
            raise Exception("Not implemented in this class")

        elif api_class == "UpgradeClusterApi":
            raise Exception("Not implemented in this class")

        elif api_class == "UpgradeClusterApi":
            raise Exception("Not implemented in this class")

        elif api_class == "WormApi":
            raise Exception("Not implemented in this class")

        elif api_class == "ZonesApi":
            raise Exception("Not implemented in this class")

        elif api_class == "ZonesSummaryApi":
            raise Exception("Not implemented in this class")

        else:
            raise Exception("Not implemented in this class")
