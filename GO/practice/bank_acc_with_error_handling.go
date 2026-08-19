package main

import (
	"fmt"
	"sync"
	// Add any other necessary imports
)

// BankAccount represents a bank account with balance management and minimum balance requirements.
type BankAccount struct {
	ID         string
	Owner      string
	Balance    float64
	MinBalance float64
	mu         sync.Mutex // For thread safety
}

// Constants for account operations
const (
	MaxTransactionAmount = 10000.0 // Example limit for deposits/withdrawals
)

// Custom error types

// AccountError is a general error type for bank account operations.
// Implement this error type
type AccountError struct {
	AccountID string
	Message   string
}

// Implement error message
func (e *AccountError) Error() string {
	if e.AccountID == "" {
		return e.Message
	}
	return fmt.Sprintf("account %s: %s", e.AccountID, e.Message)
}

// InsufficientFundsError occurs when a withdrawal or transfer would bring the balance below minimum.
// Implement this error type
type InsufficientFundsError struct {
	AccountID  string
	Balance    float64
	MinBalance float64
	Requested  float64
}

// Implement error message
func (e *InsufficientFundsError) Error() string {
	return fmt.Sprintf(
		"account %s: insufficient funds: balance %.2f, min balance %.2f, requested %.2f",
		e.AccountID, e.Balance, e.MinBalance, e.Requested,
	)
}

// NegativeAmountError occurs when an amount for deposit, withdrawal, or transfer is negative.
// Implement this error type
type NegativeAmountError struct {
	Amount float64
}

// Implement error message
func (e *NegativeAmountError) Error() string {
	return fmt.Sprintf("amount cannot be negative: %.2f", e.Amount)
}

// ExceedsLimitError occurs when a deposit or withdrawal amount exceeds the defined limit.
// Implement this error type
type ExceedsLimitError struct {
	Amount float64
	Limit  float64
}

// Implement error message
func (e *ExceedsLimitError) Error() string {
	return fmt.Sprintf("amount %.2f exceeds transaction limit %.2f", e.Amount, e.Limit)
}

// NewBankAccount creates a new bank account with the given parameters.
// It returns an error if any of the parameters are invalid.
// Implement account creation with validation
func NewBankAccount(id, owner string, initialBalance, minBalance float64) (*BankAccount, error) {
	if id == "" {
		return nil, &AccountError{Message: "account id cannot be empty"}
	}
	if owner == "" {
		return nil, &AccountError{AccountID: id, Message: "account owner cannot be empty"}
	}
	if initialBalance < 0 {
		return nil, &AccountError{AccountID: id, Message: "minimum balance cannot be negative"}
	}
	if initialBalance < minBalance {
		return nil, &AccountError{
			Message: fmt.Sprintf(
				"initial balance %.2f is below minimum balance %.2f",
				initialBalance, minBalance,
			),
		}
	}

	return &BankAccount{
		ID:         id,
		Owner:      owner,
		Balance:    initialBalance,
		MinBalance: minBalance,
	}, nil
}

// Deposit adds the specified amount to the account balance.
// It returns an error if the amount is invalid or exceeds the transaction limit.
// Implement deposit functionality with proper error handling
func (a *BankAccount) Deposit(amount float64) error {
	if amount < 0 {
		return &NegativeAmountError{Amount: amount}
	}
	if amount > MaxTransactionAmount {
		return &ExceedsLimitError{Amount: amount, Limit: MaxTransactionAmount}
	}

	a.mu.Lock()
	defer a.mu.Unlock()

	a.Balance += amount
	return nil
}

// Withdraw removes the specified amount from the account balance.
// It returns an error if the amount is invalid, exceeds the transaction limit,
// or would bring the balance below the minimum required balance.
// Implement withdrawal functionality with proper error handling
func (a *BankAccount) Withdraw(amount float64) error {
	if amount < 0 {
		return &NegativeAmountError{Amount: amount}
	}
	if amount > MaxTransactionAmount {
		return &ExceedsLimitError{Amount: amount, Limit: MaxTransactionAmount}
	}

	a.mu.Lock()
	defer a.mu.Unlock()

	if a.Balance-amount < a.MinBalance {
		return &InsufficientFundsError{
			AccountID:  a.ID,
			Balance:    a.Balance,
			MinBalance: a.MinBalance,
			Requested:  amount,
		}
	}

	a.Balance -= amount
	return nil
}

// Transfer moves the specified amount from this account to the target account.
// It returns an error if the amount is invalid, exceeds the transaction limit,
// or would bring the balance below the minimum required balance.
// Implement transfer functionality with proper error handling
func (a *BankAccount) Transfer(amount float64, target *BankAccount) error {
	if target == nil {
		return &AccountError{AccountID: a.ID, Message: "target account cannot be nil"}
	}
	if amount < 0 {
		return &NegativeAmountError{Amount: amount}
	}
	if amount > MaxTransactionAmount {
		return &ExceedsLimitError{Amount: amount, Limit: MaxTransactionAmount}
	}

	if a == target {
		return &AccountError{Message: "cannot transfer to the same account"}
	}

	first, second := a, target
	if a.ID > target.ID {
		first, second = target, a
	}

	first.mu.Lock()
	defer first.mu.Unlock()
	second.mu.Lock()
	defer second.mu.Unlock()

	if a.Balance-amount < a.MinBalance {
		return &InsufficientFundsError{
			AccountID:  a.ID,
			Balance:    a.Balance,
			MinBalance: a.MinBalance,
			Requested:  amount,
		}
	}

	a.Balance -= amount
	target.Balance += amount

	return nil
}
