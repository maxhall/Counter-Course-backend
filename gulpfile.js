var gulp = require('gulp'),
    sass = require('gulp-ruby-sass');

gulp.task('styles', function() {
    return sass('app/static/scss/styles.scss', { style: 'expanded' })
	.pipe(gulp.dest('app/static/css'));
});

gulp.task('watch', function() {
    gulp.watch('app/static/scss/*.scss', ['styles']);
});

gulp.task('default', ['styles']);
