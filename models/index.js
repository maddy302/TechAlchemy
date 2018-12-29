require('./users');
require('./tag');
require('./topic');
require('./comment');

var mongoose = require('mongoose');
var config   = require('../config');
var database = config.database;

mongoose.connect("mongodb://root:abc123@ds111082.mlab.com:11082/techalchemy", {
  server: {poolSize: 20}
}, function (error) {
	if (error) {
		console.log('connect to '+database.address+' error: '+error.message);
		process.exit(1);
	}
});

exports.Users = mongoose.model('Users');
exports.Tag = mongoose.model('Tag');
exports.Topic = mongoose.model('Topic');
exports.Comment = mongoose.model('Comment');


