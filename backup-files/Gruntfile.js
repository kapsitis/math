//require("load-grunt-tasks")(grunt); // npm install --save-dev load-grunt-tasks

module.exports = function(grunt) {

    require("load-grunt-tasks")(grunt);

    grunt.initConfig({
        "babel": {
            options: {
                sourceMap: true
            },
            dist: {
                files: [
                    {
                        expand: true,
                        cwd: 'myjs/',
                        src: ['*.js'],
                        dest: 'dist_myjs/'
                    }
                ]
            }
        }
    });

    grunt.registerTask("default", ["babel"]);

};


//require("load-grunt-tasks")(grunt); // npm install --save-dev load-grunt-tasks
