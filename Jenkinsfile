pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-app:${BUILD_NUMBER} .'
                sh 'docker tag python-app:${BUILD_NUMBER} python-app:latest'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Запускаємо тести в тому ж контейнері, який ми щойно зібрали
                sh '''
                docker run --rm python-app:latest pip install pytest requests
                docker run --rm python-app:latest pytest test_app.py -v
                '''
            }
        }
        
        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up -d'
            }
        }
        
        stage('Verify Deployment') {
            steps {
                sh 'sleep 5' // Wait for container to fully start
                sh 'curl -f http://localhost:5000/api/health || exit 1'
            }
        }
    }
    
    post {
        always {
            sh 'docker image prune -f'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
