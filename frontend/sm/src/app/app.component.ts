import { Component,ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { AddStudentDialogComponent } from './add-student-dialog/add-student-dialog.component';
import { UpdateStudentComponent } from './update-student/update-student.component';
import { StudentService } from './student.service';
import { Student } from './student.model';
import { StudentListComponent } from './student-list/student-list.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Student Management System';
  SearchFilter: string = '';


  constructor(private dialog: MatDialog, private studentService: StudentService) {}
  
  openAddStudentDialog(): void {
    const dialogRef = this.dialog.open(AddStudentDialogComponent, {
      width: '400px'
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        console.log('Dialog was closed with result:', result);
        this.addStudent(result);
      }
    });
  }

  openUpdateOptionsDialog(): void {
    const dialogRef = this.dialog.open(UpdateStudentComponent, {
      width: '400px'
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        console.log('Dialog was closed with result:', result);
        this.updateStudent(result);
      }
    });
  }

  addStudent(student: Student): void {
    this.studentService.addStudent(student).subscribe(
      (response: any) => {
        console.log('Student added successfully:', response);
      },
      (error: any) => {
        console.error('Error adding student:', error);
      }
    );
  }

  updateStudent(updatedStudent: Student): void {
    this.studentService.updateStudent(updatedStudent).subscribe(
      (response: any) => {
        console.log('Student updated successfully:', response);
      },
      (error: any) => {
        console.error('Error updating student:', error);
      }
    );
  }
}


