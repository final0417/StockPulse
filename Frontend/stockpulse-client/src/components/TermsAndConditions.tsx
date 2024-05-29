import React, { useState } from 'react';

interface TermsAndConditionsProps {
  onAccept: () => void;
}

const TermsAndConditions: React.FC<TermsAndConditionsProps> = ({ onAccept }) => {
  const [accepted, setAccepted] = useState<boolean>(false);

  const handleAccept = () => {
    setAccepted(true);
    onAccept();
  };

  return (
    <div>
      <h2 className='hover:bg-slate-700 rounded-lg'>Terms and Conditions </h2>
      <div>
        <input
          type="checkbox"
          id="acceptCheckbox"
          checked={accepted}
          onChange={() => setAccepted(!accepted)}
        />
        <label htmlFor="acceptCheckbox">I have read and accept the terms and conditions</label>
      </div>
      <button disabled={!accepted} onClick={handleAccept}></button>
    </div>
  );
};

export default TermsAndConditions;