$(document).ready(function() {
    $("#loading").fadeOut(function() {
        $(this).remove(); // Optional if it's going to only be used once.
    });
    $('.menu-button').click(function() {
        if ($('.header-menu:visible').length > 0) {
            $('.header-menu').css('display', 'none');
            $('.header-top').css('display', 'block');
            $('html').css({
                'overflow': 'visible'
            });

        } else {
            $('.header-menu').css('display', 'block');
            $('.header-top').css('display', 'none');
            $('html').css({
                'overflow': 'hidden'
            });


        }
    });
    $('#carousel-fixed-height, #bs-carousel').carousel({
        interval: 3000
    });
    $(".gallery .filter-button").click(function() {
        var value = $(this).attr('data-filter');

        if (value == "all") {
            //$('.filter').removeClass('hidden');
            $('.filter').show('1000');
        } else {
            //            $('.filter[filter-item="'+value+'"]').removeClass('hidden');
            //            $(".filter").not('.filter[filter-item="'+value+'"]').addClass('hidden');
            $(".filter").not('.' + value).hide('3000');
            $('.filter').filter('.' + value).show('3000');

        }
    });
    $(".gallery2 .filter-button").click(function() {
        var value = $(this).attr('data-filter');

        if (value == "all") {
            //$('.filter').removeClass('hidden');
            $('.filter').show('1000');
        } else {
            //            $('.filter[filter-item="'+value+'"]').removeClass('hidden');
            //            $(".filter").not('.filter[filter-item="'+value+'"]').addClass('hidden');
            $(".filter").not('.' + value).hide('3000');
            $('.filter').filter('.' + value).show('3000');

        }
    });
    $("#product_menu").hide();
    $("#link_produits").mouseover(function() {
        $("#product_menu").show();
        $("#product_menu").addClass('slideUp');
    });
    $(window).mouseenter(function(event) {
        if (!$(event.target).closest('nav, #product_menu, .header-menu.mini').length) {
            $("#product_menu").hide();
            $('.header-menu.mini').css('display', 'none');
            $('html').css({
                'overflow': 'visible'
            });

        }
    });
    $('.nav-link, .nav-logo').mouseover(function(event) {
        if (!$(event.target).closest('#link_produits').length) {
            $("#product_menu").hide();
        }
    });
    $('.mini-links .categories .back').click(function() {
        $('#mini_product_menu').hide();
    });
    $(".gallery2 .gallery_product").mouseover(function() {
        $(this).find('.overlay').css('display', 'block');
        $(this).find('img').toggleClass("hover");
    });
    $(".gallery2 .gallery_product").mouseout(function() {
        $(this).find('.overlay').css('display', 'none');
        $(this).find('img').toggleClass("hover");
    });

});

function openMenu(evt, menu) {
    $('.categories').removeClass('slideout');
    var i, tabcontent, tablinks;
    $('.mini .categories').hide();
    $('#' + menu).show();
}