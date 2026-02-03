# remote-pet-feeder-aws-iot
A serverless IoT-based Remote Pet Feeder system built using AWS IoT Button, AWS Lambda, and Amazon DynamoDB. Users can remotely dispense pet food using a physical IoT button, while DynamoDB tracks feeding schedules and food dispense history.
🐾 Remote Pet Feeder using AWS IoT Button
📌 Project Overview
This project implements a Remote Pet Feeder System that allows users to dispense food for their pets by pressing a physical AWS IoT Button.
When the button is pressed:
An AWS Lambda function is triggered
The feeder is activated
Feeding data is stored in Amazon DynamoDB
This system helps pet owners manage feeding schedules remotely and track feeding history.
🛠️ Technologies Used
AWS IoT Button
AWS Lambda

Amazon DynamoDB
Python
AWS IoT Core
JSON
🏗️ Architecture
AWS IoT Button
     ↓
AWS IoT Core
     ↓
AWS Lambda
     ↓
Amazon DynamoDB
     ↓
Pet Feeder Activated
🚀 Features
Remote food dispensing via IoT button
Serverless architecture
Feeding schedule tracking
Feeding history storage
Scalable and reliable design
📂 Repository Structure
remote-pet-feeder-aws-iot/
│
├── README.md
│
├── report/
│   └── project-report.md
│
├── lambda/
│   └── feeder_handler.py
│
├── dynamodb/
│   └── table-schema.json
│
├── iot/
│   └── button-payload.json
│
├── architecture/
│   └── architecture-diagram.png
│
└── docs/
    ├── setup-guide.md
    └── workflow.md
    ⚙️ Setup Overview
Configure AWS IoT Button
Create IoT rule to trigger Lambda
Create DynamoDB table
Deploy Lambda function
Test feeder activation
✅ Outcome
Remote-controlled pet feeding
Automated feeding logs
Cloud-based IoT solution
📌 Abstract
This project presents a Remote Pet Feeder System that enables pet owners to dispense food remotely using an AWS IoT Button. The system uses AWS Lambda for event processing and Amazon DynamoDB to store feeding schedules and feeding history.
📌 Problem Statement
Pet owners are often away from home and may miss scheduled feeding times. Manual feeding systems lack remote control and tracking.
📌 Solution
The system allows users to remotely dispense food using a physical IoT button and maintains feeding records in DynamoDB.
📌 Technologies
AWS IoT Button, Lambda, DynamoDB, Python
📌 Advantages
Remote pet feeding
Low latency
Serverless and scalable
Feeding history tracking
📌 Future Scope
Mobile app integration
Automated feeding schedules
Camera integration
