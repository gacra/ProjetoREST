var prices_list = [];

function TasksViewModel() {
  var self = this;
  self.plans = ko.observableArray();
  $.getJSON('http://127.0.0.1:8000/plans/?format=json', function(data) {
		$(data).each(function(index, obj) {
			self.plans.push({
				id: ko.observable(obj['id']),
				name: ko.observable(obj['name']),
			});
			prices_list.push(obj['price']);
		});
		if(plan_id >= $('#product option').length){
			plan_id = 0;
		}
		$('#product').val(plan_id+1);
		updateProductPrice();
	});
}

function updateProductPrice() {
	$("#product_price").val(prices_list[$('#product').val()-1]);
	updatePrice();
}

function updatePrice(event) {
	var product_price_input = document.getElementById("product_price");
	var discount_input = document.getElementById("discount");
	var price_input = document.getElementById("price");
	if(product_price_input.checkValidity() && discount_input.checkValidity()){
		var product_price = product_price_input.value;
		var discount = discount_input.value;
		var price = product_price * (1.0 - (discount/100.0));
		price_input.value = price.toFixed(2);
	}
}

function postREST() {
	var payment_date = $('#payment_date').val();
	var payment_type = $('[name="payment_type"]:checked').val();
	var product = $('#product').val();
	var product_price = $('#product_price').val();
	var discount = $('#discount').val();
	var transaction_id = $('#transaction_id').val();
	var body = {
		'payment_date': payment_date,
		'payment_type': payment_type,
		'product': product,
		'product_price': product_price,
		'discount': discount,
		'transaction_id': transaction_id,
		'csrfmiddlewaretoken': Cookies.get('csrftoken')
	}
	//console.log(body);
	$.post('http://127.0.0.1:8000/payment/?format=json', body, function(data, textStatus, xhr) {
		$('.invalid-id').hide();
		$('#transaction_id').removeAttr('style');
		$('.unknow_error').hide();
		$('#modal').modal({
			backdrop: 'static',
			keyboard: false
		});
	}).fail(function (data, textStatus, xhr) {
		var resp = JSON.parse(data['responseText']);
		if(typeof resp['transaction_id'] != "undefined"){
			$('.invalid-id').text(resp['transaction_id'][0]);
			$('.invalid-id').show();
			$('#transaction_id').attr("style","border-color: #dc3545; box-shadow: none;");
		}else{
			$('.invalid-id').hide();
			$('#transaction_id').removeAttr('style');
			$('.unknow_error').html("Ocorreu um erro inexperado. Mais informações abaixo." + "<br/>" + "Em caso de dúvida entre em contato com o administrador.")
			var keys = Object.keys(resp);
			for(var i=0;i<keys.length;i++){
			    var key = keys[i];
			    $('.unknow_error').append("<br/>" + "Cód: " + key + "<br/>" + " Msg: " + resp[key]);
			}
			$('.unknow_error').show();
		}
	});
}

function sendForm(){
	var form = document.getElementById("needs-validation");
	form.addEventListener("submit", function(event) {
		if (form.checkValidity() == false) {
			event.preventDefault();
			event.stopPropagation();
			$(".alert").show();
		}else{
			event.preventDefault();
			event.stopPropagation();
			postREST();
			$(".alert").hide();
		}
		form.classList.add("was-validated");
	}, false);
}

$(document).ready(function() {
	ko.applyBindings(new TasksViewModel(), $('#main')[0]);
	$("#product").on('change keyup', updateProductPrice);
	$("#discount").on('change keyup click', updatePrice);
	sendForm();
});