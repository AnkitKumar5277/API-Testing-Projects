pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/AnkitKumar5277/API-Testing-Projects.git'
            }
        }
        
        stage('Run Postman Tests') {
            steps {
                bat '''
                newman run postman/postman_collection.json ^
                -r html --reporter-html-export reports/report.html
                '''
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Postman API Test Report'
            ])
        }
    }
}
