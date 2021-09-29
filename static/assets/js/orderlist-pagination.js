$(function() {
    $('#bootstrap-table').DataTable({
        pageLength: 25,
        lengthChange: true,
        // bFilter: true,
        // autoWidth: true,
        // autoAdjustHeight: true,
        // autoplay: true,
        // lengthAdjust: false,
        // scrollY: "60vh",
        // sScrollX: "100%",
        // sScrollXInner: "50%",
        // scrollCollapse: false,
        // paging: true,
        // responsive: true,
    });
    // $('#datatables-dashboard-products').closest('.dataTables_scrollBody').css('max-height', '100%');
    $('#bootstrap-table').DataTable().draw();
});