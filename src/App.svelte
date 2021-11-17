<script>
  let requestPasswdChars = 16;
  let requestDigit = false;
  let requestPunctuation = false;
  let inputText = '';
  let generetedPasswd = '--------';

  const generatePasswd = async () => {
    // IP address is Ubuntu on Parallels
    const endpoint = 'http://10.211.55.21:8000/gen_passwd/';
    const params = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        passwd_chars: requestPasswdChars,
        request_digit: requestDigit,
        request_punctuation: requestPunctuation,
        specified_text: inputText.replace(/\s+/g, ''),
      }),
    };

    console.log(params);
    const response = await fetch(endpoint, params);
    const data = await response.json();
    console.log(data);
    generetedPasswd = data.Passwd;
  };

  export let name;
</script>

<main>
  <h1>Hello {name}</h1>

  <label>
    <p>Number of chars: {requestPasswdChars}</p>
    <input type="range" bind:value={requestPasswdChars} min="8" max="128" on:change={generatePasswd} />
  </label>

  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label>
    <p>Digit</p>
    {#if inputText.length > 0}
      <input type="checkbox" bind:checked={requestDigit} on:change={generatePasswd} disabled="disabled" />
    {:else}
      <input type="checkbox" bind:checked={requestDigit} on:change={generatePasswd} />
    {/if}
  </label>

  <!-- svelte-ignore a11y-label-has-associated-control -->
  <label>
    <p>Punctuation</p>
    {#if inputText.length > 0}
      <input type="checkbox" bind:checked={requestPunctuation} on:change={generatePasswd} disabled="disabled" />
    {:else}
      <input type="checkbox" bind:checked={requestPunctuation} on:change={generatePasswd} />
    {/if}
  </label>

  <label>
    <p>Text want to specify</p>
    <textarea maxlength="128" bind:value={inputText} on:input={generatePasswd} />
  </label>

  <div>
    <p class="passwd-title">Generated Password</p>
    <p class="passwd">{generetedPasswd}</p>
  </div>
</main>

<style>
  main {
    text-align: center;
    min-width: 320px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  .passwd-title {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 2em;
    font-weight: 100;
    background-color: #eee;
    padding: 0.5em;
  }

  .passwd {
    font-size: 1.2em;
    font-weight: 100;
    word-break: break-all;
  }
</style>
