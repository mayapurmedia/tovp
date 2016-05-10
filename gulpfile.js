/* File: gulpfile.js */

// grab our gulp packages
var gulp  = require('gulp'),
    less = require('gulp-less'),
    notify = require('gulp-notify'),
    path = require('path'),
    cssnano = require('gulp-cssnano'),
    autoprefixer = require('gulp-autoprefixer'),
    // uglify = require('gulp-uglify'),
    gutil = require('gulp-util');


gulp.task('less', function () {
  return gulp.src('./tovp/theme/less/style.less')
    .pipe(less({
      paths: [ path.join(__dirname, 'less', 'includes') ]
    }))
    .on('error', function() {
      this.emit('end');
    })
    .on("error", notify.onError(function(error) {
      return "Failed to Compile LESS: " + error.message;
    }))
    .pipe(autoprefixer())
    .pipe(cssnano())
    .pipe(gulp.dest('./tovp/theme/static/css'))
    .pipe(notify("LESS Compiled Successfully :)"));
});

// // Task to Minify JS
// gulp.task('jsmin', function() {
//   return gulp.src('./src/js/**/*.js')
//     .pipe(uglify())
//     .pipe(gulp.dest('./dist/js/'));
// });

// // create a default task and just log a message
// gulp.task('default', function() {
//   return gutil.log('Gulp is running!')
// });

// Gulp Watch Task
gulp.task('watch', function () {
   gulp.watch('./tovp/theme/less/*.*', ['less']);
});

// Gulp Default Task
gulp.task('default', ['watch']);

// // Gulp Build Task
// gulp.task('build', function() {
//   runSequence('movecss', 'imagemin', 'jsmin', 'inlinesource');
// });

