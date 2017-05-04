/* File: gulpfile.js */

// grab our gulp packages
var gulp  = require('gulp'),
    less = require('gulp-less'),
    sass = require('gulp-sass'),
    notify = require('gulp-notify'),
    path = require('path'),
    cssnano = require('gulp-cssnano'),
    autoprefixer = require('gulp-autoprefixer'),
    // uglify = require('gulp-uglify'),
    gutil = require('gulp-util');


gulp.task('less_database', function () {
  return gulp.src('./tovp/theme/less/database/style.less')
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
    .pipe(gulp.dest('./tovp/theme/static/database/css'))
    .pipe(notify("LESS Compiled Successfully :)"));
});

// Task to compile SCSS
gulp.task('sass_public', function () {
  return gulp.src('./tovp/theme/scss/public/styles.scss')
    // .pipe(sourcemaps.init())
    .pipe(sass({
      errLogToConsole: false,
      paths: [ path.join(__dirname, 'scss', 'includes', 'styles') ]
    })
    .on("error", notify.onError(function(error) {
      return "Failed to Compile SCSS: " + error.message;
    })))
    // .pipe(cssBase64())
    .pipe(autoprefixer())
    // .pipe(sourcemaps.write('./'))
    .pipe(cssnano())
    .pipe(gulp.dest('./tovp/theme/static/public/css'))
    .pipe(notify("SCSS Compiled Successfully :)"));
});

// gulp.task('less_public', function () {
//   return gulp.src('./tovp/theme/less/public/style.less')
//     .pipe(less({
//       paths: [ path.join(__dirname, 'less', 'includes') ]
//     }))
//     .on('error', function() {
//       this.emit('end');
//     })
//     .on("error", notify.onError(function(error) {
//       return "Failed to Compile LESS: " + error.message;
//     }))
//     .pipe(autoprefixer())
//     .pipe(cssnano())
//     .pipe(gulp.dest('./tovp/theme/static/public/css'))
//     .pipe(notify("LESS Compiled Successfully :)"));
// });

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
   gulp.watch('./tovp/theme/less/database/*.*', ['less_database']);
   gulp.watch('./tovp/theme/scss/public/*.*', ['sass_public']);
});

// Gulp Default Task
gulp.task('default', ['watch']);

// // Gulp Build Task
// gulp.task('build', function() {
//   runSequence('movecss', 'imagemin', 'jsmin', 'inlinesource');
// });
