ab -c 100 -n 100 $(aws cloudformation describe-stacks --stack-name SnapStartTest --query "Stacks[0].Outputs[?OutputKey=='normal'].OutputValue" --output text)

ab -c 100 -n 100 $(aws cloudformation describe-stacks --stack-name SnapStartTest --query "Stacks[0].Outputs[?OutputKey=='snapstart'].OutputValue" --output text)
