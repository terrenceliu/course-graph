const Node = require('./Node');

var course = require('./course.json');

var course_arr = Object.keys(course);

var graph = [];

for (var i = 0; i < course_arr.length; i++) {
    var course_id = course_arr[i];
    var temp_node = new Node(course_id, course[course_id].prev)
    graph.push(temp_node)
}

module.exports = graph;

