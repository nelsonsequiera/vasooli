// including plugins
// Make sure you run:
// npm install -g gulp 
// npm install gulp-less gulp-minify-css gulp-rename gulp-plumber
var gulp = require('gulp');
var less = require("gulp-less");
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var plumber = require('gulp-plumber');

// Task - Compiles Unchained Less Files
gulp.task('compile-unchained-less', function() {
    gulp.src('apps/less/apps.less') // path to your file
    .pipe(plumber())
        .pipe(less())
        .pipe(rename({
            basename: "vasooli"
        }))
        .pipe(gulp.dest('static/css'))
        .pipe(rename({
            suffix: '.min'
        }))
        .pipe(minifycss())
        .pipe(gulp.dest('static/css'));
});

// Task - Watches Unchained + unchained Less Files
gulp.task('watch', function() {
    gulp.watch('static/less/**/*.less', ['compile-unchained-less']);
    gulp.watch('static/less/*.less', ['compile-unchained-less']);
    gulp.watch('apps/**/*.less', ['compile-unchained-less']);
});

// Task - 'Gulp' Command in terminal
gulp.task('default', ['compile-unchained-less', 'watch'], function() {});