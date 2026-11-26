/**
 * @file Filter grammar for tree-sitter
 * @author Ghevira
 * @author Luthfiana
 * @license MIT
 */

/// <reference types="tree-sitter-cli/dsl" />
// @ts-check

export default grammar({
  name: 'filter',
  extras: $ => [/\s/],
  word: $ => $.identifier,
  rules: {
    query: $ => $._expr,

    _expr: $ => choice(
      $.comparison,
      $.and_expression,
      $.or_expression,
      $.not_expression,
      $.parenthesized,
    ),

    and_expression: $ => prec.left(2, seq($._expr, 'and', $._expr)),
    or_expression: $ => prec.left(1, seq($._expr, 'or', $._expr)),
    not_expression: $ => prec(3, seq('not', $._expr)),
    parenthesized: $ => seq('(', $._expr, ')'),

    comparison: $ => seq(
      $.identifier,
      choice('=', '!=', '>', '<', '>=', '<='),
      $._value,
    ),

    _value: $ => choice($.string, $.number, $.boolean),

    identifier: $ => /[a-zA-Z_][a-zA-Z0-9_.]*/,
    string: $ => /"[^"]*"/,
    number: $ => /\d+(\.\d+)?/,
    boolean: $ => choice('true', 'false'),
  }
});