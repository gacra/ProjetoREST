function TasksViewModel() {
  var self = this;
  self.plans = ko.observableArray();
  $.getJSON('http://127.0.0.1:8000/plans/?format=json', function(data) {
		$(data).each(function(index, obj) {
			self.plans.push({
				name: ko.observable(obj['name']),
	      product: ko.observable(obj['product']),
	      price: ko.observable(obj['price'].replace(/\./g, ',')),
	      description: ko.observable(obj['description']),
	      url: ko.observable('/pages/new_payment/' + (obj['id']-1)) 
			});
		});
		$("#div_plans").show();
	});
}

$(document).ready(function() {
	ko.applyBindings(new TasksViewModel(), $('#main')[0]);
});