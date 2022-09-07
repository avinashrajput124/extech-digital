








$(function () {


  var start_date1 ='';
  var end_date1 = '';
  
  if(start_date1=='' && end_date1=='')
  {
   $('#datetimepicker1').datetimepicker({
       useCurrent: false,
       
       
       format: 'DD/MM/YYYY'
   }).on('dp.change', function(e){
     console.log('here1');
     console.log(e);
  
     $(".day").click(function(){
      $("a[data-action='togglePicker']").trigger('click');
    });


     $('#datetimepicker2').data("DateTimePicker").minDate(e.date);
  
      
   });
  
  
           $('#datetimepicker2').datetimepicker({
  useCurrent: false,
  format: 'DD/MM/YYYY'
  }).on('dp.change', function(e){
  console.log(e);
  console.log('here2');
  $('#datetimepicker1').data("DateTimePicker").maxDate(e.date);
  
  
  });
  }
  
  
 
  
  
  
  
  
  
  
  });






  $("#beacon").change(function(){
    alert($(this).val());
});