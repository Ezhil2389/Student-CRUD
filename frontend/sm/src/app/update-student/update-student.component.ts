import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; // Import necessary form modules
import { StudentService } from '../student.service';
import { Student } from '../student.model';

@Component({
  selector: 'app-update-student',
  templateUrl: './update-student.component.html',
  styleUrls: ['./update-student.component.css']
})
export class UpdateStudentComponent {
  // Create a form group
  updateForm: FormGroup;

  // Define arrays for dropdown options
  options: string[] = ['GPA', 'Fee Status'];
  sections: string[] = ['A', 'B', 'C', 'D'];

  // Inject MatDialogRef and FormBuilder to handle form and dialog
  constructor(
    public dialogRef: MatDialogRef<UpdateStudentComponent>,
    private fb: FormBuilder,
    private studentService: StudentService
  ) {
    // Initialize the form group and form controls
    this.updateForm = this.fb.group({
      rollNumberUpdated: ['', Validators.required],
      updateBy: ['', Validators.required],
      gpaUpdated: [0],
      feeStatusUpdated: [false]
    });
  }

  // Function to save the updated student data and close the dialog
  saveStudent(): void {
    
    if (this.updateForm.valid) {
      console.log('Saving updated student data:', this.updateForm.value);
      const updatedStudent: Student = this.updateForm.value;

      // Call the updateStudent function of the StudentService to send data to the backend
      this.studentService.updateStudent(updatedStudent).subscribe(
        (response: any) => {
          console.log('Student updated successfully:', response);
          this.dialogRef.close();
        },
        (error: any) => {
          console.error('Error updating student:', error);
        }
      );
    } else {
      // Form is invalid, show some error message or validation indication.
    }
    
  }
}

