$(document).ready(function(){
    // Delete modal handler
    $("#deleteConfirmModal").on("show.bs.modal", function(event){
        const button = $(event.relatedTarget);        // FIXED: $() and quotes
        const contactId = button.data('id');          // FIXED: data('id')
        const deleteUrl = button.data('url');         // FIXED: data('url')
        
        $("#modal-contact-id").text(contactId);       // FIXED: .text()
        $("#confirmDeleteBtn").attr("href", deleteUrl); // FIXED: .attr()
    });
    
    // Confirm delete button handler
    $('#confirmDeleteBtn').click(function(event){
        $('#deleteConfirmModal').modal('hide');       // FIXED: .modal()
        setTimeout(() => {                            // FIXED: () =>
            window.location.href = $("#confirmDeleteBtn").attr("href");
        }, 300);
    });
});

