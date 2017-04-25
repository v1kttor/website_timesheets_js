$(function ()
{

  var start = moment().subtract(29, 'days');
  var end = moment();

    function cb(start, end)
    {
    $('#reportrange').on('change', 'input', function()
    {
    var first = start.format('YYYY-MM-DD');
    var last = end.format('YYYY-MM-DD');
    dates_to_url(first, last);
    });
    }

    // if (location.pathname == '/my/my_timesheets_date/') {
    //   var start = moment().subtract(29, 'days');
    //   var end = moment();
    // }
    // else {
    //   function getURLParameter(name) {
    //   return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search) || [null, ''])[1].replace(/\+/g, '%20')) || null;
    //   }
    //   start_date = getURLParameter('start');
    //   end_date = getURLParameter('end');
    //   var start = moment(start_date);
    //   var end = moment(end_date);
    //
    // }


    if (location.pathname != '/my/my_timesheets_date/') {
      function getURLParameter(name) {
      return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search) || [null, ''])[1].replace(/\+/g, '%20')) || null;
      }
      start_date = getURLParameter('start');
      end_date = getURLParameter('end');
      var start = moment(start_date);
      var end = moment(end_date);
    }


    function dates_to_url(first, last)
    {
    window.location = "/my/my_timesheets_date/?start=" + first + "&end=" + last;
    }

     $('#reportrange input').daterangepicker({
        startDate: start,
        endDate: end,
        ranges: {
           'Today': [moment(), moment()],
           'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
           'Last 7 Days': [moment().subtract(6, 'days'), moment()],
           'Last 30 Days': [moment().subtract(29, 'days'), moment()],
           'This Month': [moment().startOf('month'), moment().endOf('month')],
           'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        }
    }, cb);
    cb(start, end);

});
