// paste in console, need to still add scrolling function

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function hoverAndClick() {
    const items = document.querySelectorAll('.item-card-thumb-container');
    
    for (let i = 0; i < items.length; i++) {
		const item = items[i];
		const event = new MouseEvent('mouseover', {'view': window, 'bubbles': true, 'cancelable': true});
        item.dispatchEvent(event);
        console.log("Hovered over item:", item);
        const addToCartButton = item.querySelector('.add-to-cart-btn-container .btn-primary-md.add-to-cart');
        
       	if (addToCartButton) {
            console.log("Button found, clicking...");
            addToCartButton.click();
			console.log("Button should have been clicked.");
			await sleep(2000);
        }
		else {
            console.log("Button not found for this item.");
        }
	  }
}

hoverAndClick();
