import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; // Import necessary form modules
import { StudentService } from '../student.service';
import { Student } from '../student.model';

@Component({
  selector: 'app-add-student-dialog',
  templateUrl: './add-student-dialog.component.html',
  styleUrls: ['./add-student-dialog.component.css']
})
export class AddStudentDialogComponent {
  // Create a form group
  studentForm: FormGroup;

  // Define arrays for dropdown options
  classes: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'];
  sections: string[] = ['A', 'B', 'C', 'D'];

  // Inject MatDialogRef and FormBuilder to handle form and dialog
  constructor(
    public dialogRef: MatDialogRef<AddStudentDialogComponent>,
    private fb: FormBuilder,
    private studentService: StudentService
  ) {
    // Initialize the form group and form controls
    this.studentForm = this.fb.group({
      name: ['', Validators.required],
      rollNumber: ['', Validators.required],
      selectedClass: ['', Validators.required],
      selectedSection: ['', Validators.required],
      classTeacher: ['', Validators.required],
      gpa: [0, Validators.required],
      feeStatus: [false]
    });
  }

  // Function to save the new student data and close the dialog
  saveStudent(): void {
    if (this.studentForm.valid) {
      console.log('Added student data:', this.studentForm.value);
      const newStudent: Student = this.studentForm.value;

      // Call the addStudent function of the StudentService to send data to the backend
      this.studentService.addStudent(newStudent).subscribe(
        (response: any) => {
          console.log('Student added successfully:', response);
          this.dialogRef.close();
        },
        (error: any) => {
          console.error('Error adding student:', error);
        }
      );
    } else {
      // Form is invalid, show some error message or validation indication.
    }
  }
}
