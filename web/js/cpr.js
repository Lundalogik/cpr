var cpr = {
	init : function(){

		//Setup oridomi
		var oriDomiSetup = {
			  	vPanels: 		2,
			  	speed:          50,  // folding duration in ms
			  	perspective:    800,   // smaller values exaggerate 3D distortion
			
		};
		
		var panels = ["crm-panel", "sales-panel", "products-panel"];
      
      	$.each(panels, function(key, val){
	      	panels[val] = new OriDomi('.' + val +' .panel-body',oriDomiSetup ).accordion(100);
	      	
    	});

    	$(".panel").click(function(e) {
      	  var classNames = $(this).attr("class").split(' ');
          if (!e.isDefaultPrevented()) {
            var me = $(this);
           panels[classNames[0]].wait(1000).setSpeed(1500).accordion(0);
           if (!me.hasClass("expanded")) {
              me.addClass("expanded");
              $('#main-container').animate({scrollLeft: me.offset().left}, {duration: 500, easing: 'linear'});
            }
          }
      	});

        $(".close-button").click(function(e) {
          var panel = $(this).closest('.panel');
          var classNames = panel.attr("class").split(' ');
          if (panel.hasClass('expanded')) {
            e.preventDefault();
            panels[classNames[0]].setSpeed(700).accordion(90);
            $('#main-container').animate({scrollLeft: 0}, {duration: 500, easing: 'linear'});
            if (panel.hasClass('products-panel')) {
              setTimeout(function() {
                panel.removeClass("expanded");
              }, 50);
            } else {
              panel.removeClass("expanded");
            }
          }
        });
  
      	//Get articel data
		$.getJSON("/articles", function(data) { 
			var vm = new viewModel(data);
			console.log(ko.mapping.toJS(vm));
			ko.applyBindings(vm);

		});
	}
};

/**
ViewModel
*/
var viewModel = function(rawData){
	var self = this;


	//Fix articels
	$(rawData.articles).each(function(index,article){
		article.isSelected = ko.observable(false);

		article.select = function(article){
		if(article.isSelected()){
			article.isSelected(false);
			self.selectedArticles.remove(article)
		}else{
			article.isSelected(true);
			self.selectedArticles.push(article)
		}
	}
	});
	rawData.articles = listToMatrix(rawData.articles, 3);
	self.data = ko.mapping.fromJS(rawData);

	//Keep track of selected articles
	self.selectedArticles = ko.observableArray();

	//Return selected articles to server
	self.returnReturnArticles = ko.computed(function(){
		return JSON.stringify({articles:ko.toJS(self.selectedArticles())})
	});


	/* 	---------------------------
		GUI 
		---------------------------
	*/

	//Startview
	self.showStartOverlay = ko.observable(true);

	//Checkout
	self.showCheckoutOverlay = ko.observable(false);



}

function listToMatrix(list, elementsPerSubArray) {
    var matrix = [], i, k;
    for (i = 0, k = -1; i < list.length; i++) {
        if (i % elementsPerSubArray === 0) {
            k++;
            matrix[k] = [];
        }
        matrix[k].push(list[i]);
    }
    return matrix;
}

ko.bindingHandlers.fadeVisible = {
    init: function(element, valueAccessor) {
        // Initially set the element to be instantly visible/hidden depending on the value
        var value = valueAccessor();
        $(element).toggle(ko.unwrap(value)); // Use "unwrapObservable" so we can handle values that may or may not be observable
    },
    update: function(element, valueAccessor) {
        // Whenever the value subsequently changes, slowly fade the element in or out
        var value = valueAccessor();
        ko.unwrap(value) ? $(element).fadeIn() : $(element).fadeOut();
    }
};

/**
Lets get this party on the road
*/
$(function(){
	$(document).ready(function(){
		cpr.init();

	})
	
});





