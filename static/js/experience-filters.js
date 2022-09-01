const professional_checkbox = document.getElementById("professional-check");
const academic_checkbox = document.getElementById("academic-check");
const no_experiences = document.querySelector(".no-experiences")
const all_experiences = document.querySelector(".all-experiences")
const academic_experiences = document.querySelector(".academic-experiences");
const professional_experiences = document.querySelector(".professional-experiences");
const experience_filters = document.querySelector(".experience-filters")

experience_filters.addEventListener("click", () => {
    if (professional_checkbox.checked && !academic_checkbox.checked) {
        no_experiences.classList.add("hidden");
        all_experiences.classList.add("hidden");
        professional_experiences.classList.remove("hidden");
        academic_experiences.classList.add("hidden");
    }

    if (!professional_checkbox.checked && !academic_checkbox.checked) {
        all_experiences.classList.add("hidden");
        professional_experiences.classList.add("hidden");
        academic_experiences.classList.add("hidden");
        no_experiences.classList.remove("hidden");
    }

    if (professional_checkbox.checked && academic_checkbox.checked) {
        no_experiences.classList.add("hidden");
        professional_experiences.classList.add("hidden");
        academic_experiences.classList.add("hidden");
        all_experiences.classList.remove("hidden");
    }

    if (!professional_checkbox.checked && academic_checkbox.checked){
        no_experiences.classList.add("hidden");
        all_experiences.classList.add("hidden");
        professional_experiences.classList.add("hidden");
        academic_experiences.classList.remove("hidden");
    }
})

//professional_checkbox.addEventListener("change", () => {
//    if (professional_checkbox.checked && !academic_checkbox.checked) {
//        professional_experiences.classList.remove("hidden");
//    }else if (!professional_checkbox.checked) {
//        professional_experiences.classList.add("hidden");
//    }else if (professional_checkbox && academic_checkbox) {
//        professional_experiences.classList.add("hidden");
//        academic_experiences.classList.add("hidden");
//        all_experiences.classList.remove("hidden");
//


//academic_checkbox.addEventListener("change", () => {
//    if (academic_checkbox.checked && !professional_checkbox.checked) {
//        academic_experiences.classList.remove("hidden");
//    }else if (!professional_checkbox.checked) {
//        professional_experiences.classList.add("hidden");
//    }else if (professional_checkbox && academic_checkbox) {
//        professional_experiences.classList.add("hidden");
//        academic_experiences.classList.add("hidden");
//        all_experiences.classList.remove("hidden");
//
//    }
//})