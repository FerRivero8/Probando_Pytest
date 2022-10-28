pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('pip') {
      steps {
        bat 'pytest -v .'
      }
    }
  }
}
