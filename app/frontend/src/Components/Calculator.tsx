import React, { useState } from 'react';
import axios from 'axios';

const Calculator = () => {
  const [operand1, setOperand1] = useState(0);
  const [operand2, setOperand2] = useState(0);
  const [operator, setOperator] = useState('+');
  const [result, setResult] = useState('');

  const calculate = async () => {
    try {
      const response = await axios.post('http://localhost:8000/calculate',
{
      operand1,
      operand2,
      operator,
      });
      setResult(response.data.result);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <input type="number" value={operand1} onChange={(e) => setOperand1(Number(e.target.value))} />
      <select value={operator} onChange={(e) => setOperator(e.target.value)}>
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
      </select>
      <input type="number" value={operand2} onChange={(e) => setOperand2(Number(e.target.value))} />
      <button onClick={calculate}>Calculate</button>
      <div>Result: {result}</div>
    </div>
  );
};

export default Calculator;
