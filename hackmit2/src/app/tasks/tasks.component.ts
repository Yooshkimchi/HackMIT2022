import { Component, OnInit } from '@angular/core';
import { Task } from '../interfaces';

const ELEMENT_DATA: Task[] = [
  {status:1, priority:5, start_time:15, date:'this date', day:"Wednesday", duration:60, content:"Do your chores!!"},
  {status:0, priority:5, start_time:30, date:'this date', day:"Friday", duration:60, content:"Do your work!!"},
  {status:0, priority:4, start_time:45, date:'this date', day:"Thursday", duration:30, content:"Do your mate!!"},
  {status:1, priority:3, start_time:75, date:'this date', day:"Monday", duration:15, content:"Go to Gym!!"}
  
];

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  displayedColumns: string[] = ['status', 'priority', 'start', 'content'];
  dataSource = ELEMENT_DATA;


}
