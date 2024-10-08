# Desktop Agent

Desktop Agent is a comprehensive employee tracking tool designed to monitor user activity on a desktop. This project aims to provide a robust solution for tracking and analyzing employee activities to ensure productivity and compliance.

## Description

Desktop Agent allows employers to track various user activities such as mouse movements, keyboard movements, and taking screenshots at regular intervals. This tool helps in monitoring employee performance and ensuring that company resources are being used effectively.

## Features

- **User Activity Tracking**: Track mouse movements, keyboard movements, and take screenshots at regular intervals.
- **Activity Logs**: Maintain detailed logs of user activities for review and analysis.
- **Screenshot Capture**: Automatically capture screenshots at specified intervals.
- **Single Instance Enforcement**: Ensure that only one instance of the application can run at a time to prevent conflicts.
- **AWS Integration**: Store activity logs and screenshots securely on AWS.
- **User-Friendly Interface**: Easy-to-use interface for setting up and managing tracking parameters.



## Installation

To install Desktop Agent, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/PankajAjmera1/Desktop_agent.git
    ```

2. Create a `.env` file and add your AWS credentials:
    ```env
    AWS_ACCESS_KEY=your_aws_access_key
    AWS_SECRET_KEY=your_aws_secret_key
    ```
3. Navigate to the project directory:
    ```sh
    cd workstatus_agent
    ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```


## Usage

To use Desktop Agent, follow these steps:

1. Run the main application:
    ```sh
    python .\workstatus_agent\main.py
    ```
2. Configure tracking settings and monitor activities:
   +   Use the interface to set up and monitor  employee activities.
3. Change screenshot settings:

   +  If you want to modify settings like the screenshot interval or blur functionality, go to `config.json`.

## Contributing

We welcome contributions to improve Desktop Agent. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature/your-feature-name
    ```
5. Create a new Pull Request.

## Contributors

- **Pankaj Ajmera**
- **Rishabh Kushwah**
- **Laksh Sharma**
- **Prajaul Jain**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Information

For any questions or suggestions, feel free to contact:

- **Pankaj Ajmera**
- GitHub: [PankajAjmera1](https://github.com/PankajAjmera1)
- **Rishabh Kushwah**
- GitHub: [Rishabh2457](https://github.com/Rishabh2457/Desktop_agent)
- **Laksh Sharma**
- GitHub: [LakshSharma888](https://github.com/LakshSharma888/Desktop_agent)
- **Prajaul Jain**
- GitHub: [Prajauljain](https://github.com/Prajauljain/Desktop_agent)



![Output Image](./images/demo_python.png)
