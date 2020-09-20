import { Component, OnInit } from '@angular/core';
import { EmojiApi } from './services/emojis.api';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  constructor(private emojiApi: EmojiApi) {}

  public emojis = [];
  public searchInput = '';

  searchEmojis(query) {
    this.emojiApi.getEmojis(query).subscribe((emojis) => {
      this.emojis = emojis;
    });
  }

  ngOnInit() {
    this.searchEmojis('');
  }

}
