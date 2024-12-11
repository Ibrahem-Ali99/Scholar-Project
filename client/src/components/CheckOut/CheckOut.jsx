import { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import styles from './CheckOut.module.css';

function CheckoutPage() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const [course, setCourse] = useState(null);
  const [formData, setFormData] = useState({
    country: 'Egypt',
    zipCode: '',
    cardName: '',
    cardNumber: '',
    expiry: '',
    securityCode: '',
  });

  useEffect(() => {
    console.log('Received courseId:', courseId);
    fetch(`http://localhost:5000/courses/${courseId}`)
      .then((response) => response.json())
      .then((data) => setCourse(data))
      .catch((error) => console.error('Error fetching course:', error));
  }, [courseId]);
  
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handlePayment = () => {
    fetch('http://localhost:5000/process-payment', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ courseId }),
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message);
        if (data.message === 'Payment Successful') {
          navigate('/thank-you');
        }
      })
      .catch((error) => alert('Payment failed', error));
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.header}>Checkout</h1>
      {course ? (
        <div className={styles.flexContainer}>
          <div className={styles.formSection}>
            <h2>Billing Address</h2>
            <label className={styles.label}>Country</label>
            <select
              name="country"
              value={formData.country}
              onChange={handleInputChange}
              className={styles.select}
            >
              <option>Egypt</option>
              <option>United States</option>
              <option>Canada</option>
              <option>United Kingdom</option>
            </select>
            <label className={styles.label}>ZIP Code (Required)</label>
            <input
              type="text"
              name="zipCode"
              value={formData.zipCode}
              onChange={handleInputChange}
              required
              className={styles.input}
            />
            <h2>New Payment Card</h2>
            <label className={styles.label}>Name on Card</label>
            <input
              type="text"
              name="cardName"
              value={formData.cardName}
              onChange={handleInputChange}
              className={styles.input}
            />
            <label className={styles.label}>Card Number</label>
            <input
              type="text"
              name="cardNumber"
              value={formData.cardNumber}
              onChange={handleInputChange}
              className={styles.input}
            />
            <label className={styles.label}>Expiry Date (MM/YY)</label>
            <input
              type="text"
              name="expiry"
              value={formData.expiry}
              onChange={handleInputChange}
              className={styles.input}
            />
            <label className={styles.label}>Security Code</label>
            <input
              type="text"
              name="securityCode"
              value={formData.securityCode}
              onChange={handleInputChange}
              className={styles.input}
            />
            <button onClick={handlePayment} className={styles.button}>
              Complete Payment
            </button>
          </div>
          <div className={styles.summarySection}>
            <h2>Summary</h2>
            <img src={`../../assets/${course.image_url}`} alt={course.course_name} className={styles.courseImage} />
            <p>Course: {course.course_name}</p>
            <p>Original Price: ${course.price.toFixed(2)}</p>
            <p>Subtotal: ${course.price.toFixed(2)}</p>
            <p>Estimated Tax: $0.00</p>
            <h3>Total: ${course.price.toFixed(2)}</h3>
          </div>
        </div>
      ) : (
        <p>Loading course details...</p>
      )}
    </div>
  );
}

export default CheckoutPage;