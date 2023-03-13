pipeline {
    agent any
    parameters{
        string(name:'branch',defaultValue:'main')
        string(name:'imagename',defaultValue:'bookingconf')
        string(name:'appname',defaultValue:'bookingconf_service')
        string(name:'port',defaultValue:'8002')
    }
    stages {
        stage('git') {
            steps {
                git branch: "${params.branch}", url: 'https://github.com/aguywithnojob/confbooking-api'
            }
        }
        stage('build') {
            steps {
                sh 'docker build -t "${params.bookingconf}" .'
            }
        }
        stage('run') {
            steps {
                sh 'docker run --name "${params.appname}" -d -p "${params.port}":"${params.port}" $params.bookingconf'
                sh 'running on 0.0.0.0:"${params.port}"'
            }
        }
    }
}