from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.cloudformation.checks.resource.base_resource_check import BaseResourceCheck

class InstanceType(BaseResourceCheck):
    def __init__(self):
        # raise Exception("Error")
        name = "Ensure all EC2 instances are T2.Micro"
        id = "CKV_AWS_998"
        supported_resources = ("AWS::EC2::Instance",)
        categories = [CheckCategories.GENERAL_SECURITY]
        # print("test test test")
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    # def get_evaluated_keys(self):
    #     print(self)
    #     return ['instance_type']

    def scan_resource_conf(self, conf):
        # raise Exception("Error")
        # print(conf)
        properties = conf.get('Properties', {})

        if properties.get('InstanceType') == 't2.micro':
            return CheckResult.PASSED
        else:
            return CheckResult.FAILED

check = InstanceType()
