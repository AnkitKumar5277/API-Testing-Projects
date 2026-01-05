pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: '<your-repo-url>'
            }
        }

        stage('Run Postman Tests') {
            steps {
                bat '''
                newman run postman/collection.json ^
                -e postman/environment.json ^
                -r html --reporter-html-export reports/report.html
                '''
            }
        }
    }

    post {
        always {
            publishHTML([
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Postman API Test Report'
            ])
        }
    }
}
