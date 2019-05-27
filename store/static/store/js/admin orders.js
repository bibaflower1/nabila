/*  global $, alert, console */

$(function() {

    'use strict';

    //Adjust Header Height

    /*var myHeader = $('.meals-res');

    myHeader.height($(window).height());

    $(window).resize( function() {

        myHeader.height($(window).height())
    });*/

   // Adjust BxSlider List Item Center 
    
    $('.slider').each(function(){

        $(this).css('paddingTop', ($('.slider').height() - $('.intro').height()) /2)
        
    })

   /* $('.add-food').each(function(){

        $(this).css('paddingTop', ($(window).height() -( $('header').height()+$('footer'))))
        
    })*/

    $('.about').each(function(){

        $(this).css('paddingTop', ($('.about').height() - $('.about-us').height()) /2)
        
    })

})

