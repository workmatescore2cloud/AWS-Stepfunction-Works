# AWS Step Functions - Serverless Daycare Registration System

## Overview
This hands-on demo will guide users through creating a **serverless workflow** to automate daycare registration using **AWS Step Functions, Lambda, DynamoDB, and API Gateway**.

## Architecture Diagram

## Key Features
- **Automated workflow** for daycare registration.
- **Serverless architecture** leveraging AWS Step Functions.
- **Data validation and processing** using AWS Lambda.
- **Secure data storage** with Amazon DynamoDB.
- **Parent notification system** via Amazon SNS.
- **Logging and monitoring** using AWS CloudWatch Logs.

## Steps to Deploy
### **1. Create an AWS Step Functions State Machine**
- Define the state machine workflow in **AWS Step Functions**.
- Specify the sequence of states for registration, validation, and notification.

### **2. Integrate AWS Lambda for Data Processing**
- Create Lambda functions to handle:
  - Data validation.
  - Registration processing.
  - Parent notifications.

### **3. Store Registration Details in DynamoDB**
- Create a **DynamoDB table** to store daycare registration details.
- Configure Step Functions to write registration data to the database.

### **4. Notify Parents via SNS**
- Integrate **Amazon SNS** to send notifications to parents upon successful registration.
- Define an SNS topic and subscribe parents' contact details.

### **5. Monitor Execution Using CloudWatch Logs**
- Enable **AWS CloudWatch Logs** to track Step Function executions.
- Use CloudWatch for debugging and performance analysis.

## Prerequisites
- **AWS Account** with access to Step Functions, Lambda, DynamoDB, API Gateway, and SNS.
- **AWS CLI** installed and configured.
- **Terraform or AWS CloudFormation** (Optional: for automated deployment).

## Deployment Guide
### **Option 1: Using AWS Console**
1. Navigate to **AWS Step Functions** and create a new state machine.
2. Define the workflow using the Step Functions JSON definition.
3. Deploy Lambda functions and link them to the workflow.
4. Set up DynamoDB, API Gateway, and SNS services.
5. Test and monitor execution via AWS Console.

### **Option 2: Using CloudFormation (Recommended)**
- Use the provided **CloudFormation template** to deploy infrastructure automatically.
- **CloudFormation Template Link:** [GitHub Repository](https://github.com/your-repo/aws-stepfunctions-daycare)

## Testing
- Trigger the API Gateway endpoint to initiate the registration.
- Verify state transitions in **AWS Step Functions Console**.
- Check DynamoDB table for registered entries.
- Confirm SNS notifications received by parents.
- Monitor logs in **AWS CloudWatch**.

## Cleanup
To avoid incurring unnecessary AWS charges, delete the resources after testing:
```bash
aws stepfunctions delete-state-machine --state-machine-arn <ARN>
aws lambda delete-function --function-name <function-name>
aws dynamodb delete-table --table-name <table-name>
aws sns delete-topic --topic-arn <ARN>
```

## Contributing
Feel free to submit **issues** or **pull requests** to improve this project.

## License
This project is licensed under the **MIT License**.

---
