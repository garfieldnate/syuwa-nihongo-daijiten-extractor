## Structure

* PDF, with and without OCR, and (garbage) TXT file from digitization of 手話・日本語大辞典 (978-4331506806) via eridian.de
* marked page numbers are 7 less than PDF numbers
* one-handed signs on pages 65-272
* two-handed signs on pages 275-488
* two-handed different-shape signs on pages 491-684
* Should double-check on each page that OCR'd data actually exists
* Entries are not split across pages, thank goodness
* Each description starts with [ac】(I think it stands for action?)
* some entries had to be split for space reasons, and the second one is marked with "説明２"
* (A), (B), etc. just mark the first, second, third time, etc. that a particular keyword is used in a definition.
* [ac] = action (movement explanation)
* [ma] = memory aid
* [us] = usage
* mouth shapes not included :(

## To Extract

* Section type (one/two/two-different)
* Page number
* ID number
* definition
    - split on ・, remove the (A), etc.
* hand shape
* one of:
    - single hand location
    - dual hand movement
    - other hand shape
* dual hand movement
* illustration (image)
* notes
    - movement explanation
    - memory aid
    - usage

## Work Log

Trying to run [layoutXLM](https://huggingface.co/docs/transformers/model_doc/layoutxlm) model over document to see what it spits out.

Sent PR: https://github.com/huggingface/transformers/pull/15293
    - PIL cannot read PDF's but the example usage documentation for `https://huggingface.co/docs/transformers/model_doc/layoutlmv2` says to go ahead and load PDF's with PIL

Split giant 800-page PDF into single pages using `pdfseparate ../SYUWA-NIHONGO\ DAIJITEN.pdf %d.pdf`.

Next: print out heights and widths for each page to see if they are consistent. Then continue with seeing if layoutXLM works.
