var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { 
    title: 'index',
  });
});
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { 
    title: 'Home',
  });
});
/* GET about page. */
router.get('/about', function(req, res, next) {
  res.render('about', { 
    title: 'About',
  });
});
/* GET products page. */
router.get('/project', function(req, res, next) {
  res.render('project', { 
    title: 'Projects',
  });
});
/* GET contact page. */
router.get('/contact', function(req, res, next) {
  res.render('contact', { 
    title: 'Contact Us',
  });
});

module.exports = router;
