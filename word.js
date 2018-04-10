function Word(x, y, data) {
	this.x = x;
	this.y = y;
	this.orglsize = data.size;
	this.size = (data.size/max_size) * 40 + 3;
	this.text = data.text;
	this.color = {
		r: random(130, 250),
		g: random(255),
		b: random(255)
	};
}