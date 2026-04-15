pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/Harshit04-S/PythonSeleniumPytestFramework.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest EndToEnd/ --junitxml=reports\\results.xml --html=reports\\report.html --self-contained-html
                '''
            }
        }

        stage('Publish Reports') {
            steps {
                junit 'reports\\results.xml'
                publishHTML([reportDir: 'reports',
                             reportFiles: 'report.html',
                             reportName: 'Pytest HTML Report'])
            }
        }
    }
}
