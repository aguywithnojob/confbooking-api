pipeline {
    agent any
    parameters{
        string(name:'branch',defaultValue:'main')
        string(name:'imagename',defaultValue:'bookingconf')
        string(name:'appname',defaultValue:'bookingconf_service')
    }
    stages {
        stage('checkout') {
            steps {
                git branch: "${params.branch}", url: 'https://github.com/aguywithnojob/confbooking-api'
            }
        }
        stage('build') {
            steps {
                sh 'docker build -t ${params.bookingconf} .'
            }
        }
        stage('deploy') {
            steps {
                sh 'docker run --name ${params.appname} -d -p 8002:8002 $params.bookingconf'
                sh 'running on 0.0.0.0:8002'
            }
        }
    }
}