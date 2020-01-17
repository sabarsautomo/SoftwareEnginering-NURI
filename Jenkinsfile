pipeline {
    agent any
    stages {
        stage('Tahap Persiapan') {
                steps {
                        echo 'Proses cek progress...'
			
                }
        }
	    stage('Tahap I'){
		    
		steps {
			input('Apakah akan diproses?')
        }
	    }
        stage('Tahap II') {
                when {
                        not {
                                branch "master"
                        }
                }
                steps {
			echo "Hello"
                        }
        }
        stage('Tahap III') {
                parallel {
                        stage('Unit Test') {
                                steps{
                                        echo "Running the unit test..."
                                }
                        }
                        stage('Integration test') {
                        agent {
                                docker {
                                        reuseNode false
					image 'ubuntu'
                                        }
			}
				steps {
					echo 'Running the integration test..'
				}
                               
			}  }
        }
    }
}

