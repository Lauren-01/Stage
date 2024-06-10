echo "cfn-lint *.yaml"
cfn-lint *.yaml

echo "cfn-lint *.yaml --ignore-templates invalid-template.yaml"
cfn-lint *.yaml --ignore-templates invalid-template.yaml
