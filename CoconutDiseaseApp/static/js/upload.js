$(document).ready(function () {
  $("#details-block").hide();
  $("#detectDiseaseForm").submit(function (event) {
    event.preventDefault();
    var formData = new FormData(this);
    showConfirmation(
      "Are you sure you want to detect the dental disease?",
      () => {
        DetectDisease(formData);
      }
    );
  });

  $("#image").change(function () {
    $("#disease_name").text("");
    $("#description").text("");
    $("#remedies").text("");
    $("#details-block").hide();
    $(".info-block").hide();
    displayImage(this);
  });
});

const displayImage = (input) => {
  var previewImage = $("#previewImage")[0];

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      previewImage.src = e.target.result;
    };

    reader.readAsDataURL(input.files[0]);
  }
};

const DetectDisease = (formData) => {
  $("#disease_name").text("");
  $("#description").text("");
  $("#remedies").text("");
  showProcessingAlert("Please wait....", false);
  PostRequest(
    "/predict_disease/",
    formData,
    (response) => {
      closeProcessingAlert();
      if (response.status) {
        const data = response.data;
        $("#disease_name").text(data.title);
        $("#description").text(data.description);
        let remediesHtml = '<ul>';
        data.remedies.forEach(function (remedy) {
          remediesHtml += `<li class="text-start">${remedy}</li>`;
        });
        remediesHtml += '</ul>';

        // Inject into the DOM
        $('#remedies').html(remediesHtml);
      } else {
        showError(response.message);
      }
    },
    true
  );
};
