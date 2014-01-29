var lbsappstore = {
	init : function(){
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
	self.test ="test"
	self.selectedArticles = ko.observableArray();
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
	self.returnReturnArticles = ko.computed(function(){
		return JSON.stringify({articles:ko.toJS(self.selectedArticles())})
	});

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

/**
Lets get this party on the road
*/
$(function(){
	$(document).ready(function(){
		lbsappstore.init();

	})
	
});





