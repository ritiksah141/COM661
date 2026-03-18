import { Component } from '@angular/core';
import { BusinessData } from '../../services/business-data';

@Component({
  selector: 'app-businesses',
  providers: [BusinessData],
  imports: [],
  templateUrl: './businesses.html',
  styleUrl: './businesses.css',
})
export class Businesses {
  businesses_list: any = [ ];
  page: number = 1;
  lastPageNumber: number = 1;

  constructor(protected businessData: BusinessData) {}

  ngOnInit() {
    if (sessionStorage['page']) {
      this.page = Number(sessionStorage['page']);
    }
    this.businesses_list = this.businessData.getBusinesses(this.page);
  }

  previousPage() {
    if (this.page > 0) {
      this.page = this.page - 1
      sessionStorage['page'] = this.page;
      this.businesses_list = this.businessData.getBusinesses(this.page);
    }
  }

  nextPage() {
    if (this.page < this.businessData.getLastPageNumber()) {
      this.page = this.page + 1;
      sessionStorage ['page'] = this.page;
      this.businesses_list = this. businessData.getBusinesses(this.page);
    }
  }
}
