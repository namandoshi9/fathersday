$(document).ready(function(){


	//back-top-top
   // jQuery('.back-to-top').click(function () {
   //      jQuery('html, body').animate({scrollTop: 0}, 800);
   //      return false;
   //  });

}); // end ready

$(window).on('load', function(){

        //loader-script

         $('#status').fadeOut(); // will first fade out the loading animation 
         $('#preloader').delay(500).fadeOut('slow'); // will fade out the white DIV that covers the website. 
         $('body').delay(500).css({
             'overflow': 'visible'
         });


        //$('#myModal').modal('show');

     

}); // end load

$(window).on('resize', function(){

    //equalheight('.main_article');

}); // end resize

$(window).on('scroll', function(){

    // ** STICKY OR FIXED JS
    // if ($(this).scrollTop() > 50){  
    //     $('.header').addClass("sticky");
    // }
    // else{
    //     $('.header').removeClass("sticky");
    // }

}); // end scroll